# -------------------------------------------------------------------------
#  Copyright 2026 Ratha SIV. All rights reserved.
#  Apache-2.0 license
# -------------------------------------------------------------------------

import os
import yaml

def load_template(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def generate_indexes(yaml_path: str, template_path: str, output_root: str = "."):
    # Load YAML
    with open(yaml_path, "r") as f:
        data = yaml.safe_load(f)

    base_url = data["base_url"]
    indexes = data["indexes"]

    # Load HTML template
    template = load_template(template_path)

    # Generate compute-platform-level index.html
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

    # Generate package-level index.html
    for entry in indexes:
        compute_platform = entry["compute_platform"]
        packages = entry["packages"]

        for pkg in packages:
            package_name = pkg["package_name"]
            release_tag = pkg["release_tag"]
            dist_files = pkg["dist"]

            out_dir = os.path.join(output_root, compute_platform, package_name)
            os.makedirs(out_dir, exist_ok=True)

            # Build the list of links
            link_lines = []
            for dist in dist_files:
                full_url = f"{base_url}/{release_tag}/{dist}"
                link_lines.append(f'<a href="{full_url}">{dist}</a><br>')

            # Fill template
            html = template.format(
                compute_platform=compute_platform,
                package_name=package_name,
                links_here="\n    ".join(link_lines)
            )

            # Write index.html
            with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as f:
                f.write(html)

            print(f"Generated: {compute_platform}/{package_name}/index.html")


if __name__ == "__main__":
    BASE_DIR = os.path.dirname(__file__)
    REPO_ROOT = os.path.abspath(os.path.join(BASE_DIR, "..", ".."))
    INDEX_OUTPUT_DIR = os.getenv("INDEX_OUTPUT_DIR", REPO_ROOT)
    indexation_yaml = os.path.join(BASE_DIR, "indexation.yaml")
    template_html_tpl = os.path.join(BASE_DIR, "template.html.tpl")
    generate_indexes(indexation_yaml, template_html_tpl, INDEX_OUTPUT_DIR)
