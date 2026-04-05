# -------------------------------------------------------------------------
#  Copyright 2026 Ratha SIV. All rights reserved.
#  Apache-2.0 license
# -------------------------------------------------------------------------

import os
import yaml

def load_template(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def generate_indexes(yaml_path: str, index_tpl_path: str, release_block_tpl_path: str, output_root: str = "."):
    # Load YAML
    with open(yaml_path, "r") as f:
        data = yaml.safe_load(f)

    dist_url = data["dist_url"]
    release_url = data["release_url"]
    indexes = data["indexes"]

    # Load templates
    main_template = load_template(index_tpl_path)
    release_block_template = load_template(release_block_tpl_path)

    # ---------------------------------------------------------------------
    # Generate compute-platform-level index.html
    # ---------------------------------------------------------------------
    for entry in indexes:
        compute_platform = entry["compute_platform"]
        platform_dir = os.path.join(output_root, compute_platform)
        os.makedirs(platform_dir, exist_ok=True)

        platform_index_path = os.path.join(platform_dir, "index.html")
        with open(platform_index_path, "w", encoding="utf-8") as f:
            f.write(f"<h2>Packages for {compute_platform}</h2>\n")
            for pkg in entry["packages"]:
                pkg_name = pkg["package_name"]
                f.write(f'<a href="{pkg_name}/index.html">{pkg_name}</a><br>\n')

    # ---------------------------------------------------------------------
    # Generate package-level index.html with multiple releases
    # ---------------------------------------------------------------------
    for entry in indexes:
        compute_platform = entry["compute_platform"]
        packages = entry["packages"]

        for pkg in packages:
            package_name = pkg["package_name"]
            releases = pkg["releases"]

            out_dir = os.path.join(output_root, compute_platform, package_name)
            os.makedirs(out_dir, exist_ok=True)

            release_blocks = []

            # Build each release block
            for rel in releases:
                version = rel["version"]
                release_tag = rel["release_tag"]
                build_log = rel["build_log"]
                dist_files = rel["dist"]

                # Build wheel links
                link_lines = []
                for dist in dist_files:
                    full_url = f"{dist_url}/{release_tag}/{dist}"
                    link_lines.append(f'<a href="{full_url}">{dist}</a><br>')

                # Fill release block template
                block_html = release_block_template.format(
                    version=version,
                    release_tag=release_tag,
                    release_url=release_url,
                    dist_url=dist_url,
                    build_log=build_log,
                    links_here="\n            ".join(link_lines)
                )

                release_blocks.append(block_html)

            # Combine all release blocks
            all_release_blocks = "\n".join(release_blocks)

            # Fill main template
            final_html = main_template.format(
                compute_platform=compute_platform,
                package_name=package_name,
                release_blocks=all_release_blocks
            )

            # Write index.html
            with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as f:
                f.write(final_html)

            print(f"Generated: {compute_platform}/{package_name}/index.html")


def update_readme_summary_table(yaml_path: str, readme_path: str):
    with open(yaml_path, "r") as f:
        data = yaml.safe_load(f)

    dist_url = data["dist_url"]
    release_url = data["release_url"]
    indexes = data["indexes"]

    rows = []

    for entry in indexes:
        compute_platform = entry["compute_platform"]
        for pkg in entry["packages"]:
            package_name = pkg["package_name"]
            releases = pkg["releases"]

            latest = releases[-1]
            version = latest["version"]
            release_tag = latest["release_tag"]

            pytorch = latest.get("pytorch", {})
            torch_ver = pytorch.get("torch", "-")
            torchvision_ver = pytorch.get("torchvision", "-")

            row = (
                f"| `{package_name}` "
                f"| `{version}` "
                f"| [`{compute_platform}`](https://rathaumons.github.io/bevfusionx-index/{compute_platform}) "
                f"| [`{release_tag}`]({release_url}/{release_tag}) "
                f"| `{torch_ver}`/`{torchvision_ver}` |"
            )

            rows.append((package_name.lower(), row))

    # Sort by package_name
    rows.sort(key=lambda x: x[0])

    # Join rows
    table_body = "\n".join(row for _, row in rows)

    # Read README
    with open(readme_path, "r", encoding="utf-8") as f:
        readme = f.read()

    # Replace the table section
    start_marker = "## Summary Table"
    end_marker = "THESE WHEELS WERE BUILT"

    start_idx = readme.index(start_marker)
    end_idx = readme.index(end_marker)

    before = readme[:start_idx]
    after = readme[end_idx:]

    new_table = (
        "## Summary Table\n\n"
        "| Package<br>Name | Latest<br>Version | Index<br>Suffix | Release<br>Tag | Built with PyTorch<br>`torch`/`torchvision` |\n"
        "| - | - | - | - | - |\n"
        f"{table_body}\n\n"
    )

    updated = before + new_table + after

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(updated)

    print("README.md summary table updated.")


# -------------------------------------------------------------------------
# Entry point
# -------------------------------------------------------------------------
if __name__ == "__main__":
    BASE_DIR = os.path.dirname(__file__)
    REPO_ROOT = os.path.abspath(os.path.join(BASE_DIR, "..", ".."))
    INDEX_OUTPUT_DIR = os.getenv("INDEX_OUTPUT_DIR", REPO_ROOT)

    indexation_yaml = os.path.join(BASE_DIR, "indexation.yaml")
    template_html_tpl = os.path.join(BASE_DIR, "index-template.html.tpl")
    release_block_tpl = os.path.join(BASE_DIR, "release-block-template.html.tpl")
    generate_indexes(indexation_yaml, template_html_tpl, release_block_tpl, INDEX_OUTPUT_DIR)

    readme_path = os.path.join(REPO_ROOT, "README.md")
    update_readme_summary_table(indexation_yaml, readme_path)

