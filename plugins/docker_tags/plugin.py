import os
import time
import json
import requests
from mkdocs.plugins import BasePlugin
from mkdocs.config import config_options

class DockerTagsPlugin(BasePlugin):
    config_scheme = (
        ('user', config_options.Type(str, required=True)),
        ('repo', config_options.Type(str, required=True)),
        ('json_output', config_options.Type(str, required=True)),
        ('page_size', config_options.Type(int, default=5)),
        ('max_pages', config_options.Type(int, default=1)),
        ('retries', config_options.Type(int, default=3)),
        ('cache_max_age', config_options.Type(int, default=3600)),
        ('md_output', config_options.Type(str, required=True)),
        ('md_pull_output', config_options.Type(str, required=True)),
        ('md_image_output', config_options.Type(str, required=True)),
    )

    def on_pre_build(self, config):
        user = self.config['user']
        repo = self.config['repo']
        output_path = self.config['json_output']
        page_size = self.config['page_size']
        max_pages = self.config['max_pages']
        retries = self.config['retries']
        cache_max_age = self.config['cache_max_age']
        md_path = self.config['md_output']
        md_pull_path = self.config['md_pull_output']
        md_image_path = self.config['md_image_output']

        # Check cache freshness
        if os.path.exists(output_path):
            age = time.time() - os.path.getmtime(output_path)
            if age < cache_max_age:
                mins = int(age // 60)
                print(f"Using cached Docker tag data (updated {mins} min ago).")
                return

        print(f"Fetching Docker Hub tags for {user}/{repo}…")

        all_tags = []
        for page in range(1, max_pages + 1):
            url = f"https://hub.docker.com/v2/repositories/{user}/{repo}/tags/?page_size={page_size}&page={page}"

            for attempt in range(retries):
                try:
                    response = requests.get(url, timeout=15)
                    response.raise_for_status()
                    data = response.json()
                    all_tags.extend(data.get("results", []))
                    break
                except requests.RequestException as e:
                    if attempt < retries - 1:
                        wait = 2 ** attempt
                        print(f"Attempt {attempt + 1} failed ({e}). Retrying in {wait}s…")
                        time.sleep(wait)
                    else:
                        print(f"Failed to fetch tags after {retries} attempts: {e}")
                        return

        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, "w") as f:
            json.dump(all_tags, f, indent=2)

        print(f"Wrote {len(all_tags)} tags to {output_path}")

        # Write Markdown table
        os.makedirs(os.path.dirname(md_path), exist_ok=True)
        with open(md_path, "w") as f:
            f.write("| Tag  | Architectures  | Size (MB)  | Last Updated  | Pull Command  |\n")
            f.write("|------|----------------|------------|---------------|---------------|\n")

            # Sort by last_updated descending
            all_tags.sort(key=lambda t: t.get("last_updated", ""), reverse=True)

            for tag in all_tags:
                name = tag.get("name", "")
                last_updated = tag.get("last_updated", "")
                if last_updated:
                    try:
                        dt = datetime.fromisoformat(last_updated.replace("Z", "+00:00"))
                        last_updated = dt.strftime("%Y-%m-%d")
                    except Exception:
                        pass

                images = tag.get("images", [])
                archs = sorted({img.get("architecture", "unknown") for img in images})
                arch_str = ", ".join(archs)

                total_size = sum(img.get("size", 0) for img in images)
                size_mb = f"{total_size / (1024 * 1024):.1f}"

                pull_cmd = f"docker pull {user}/{repo}:{name}"

                f.write(f"| `{name}` | {arch_str} | {size_mb} | {last_updated} | `{pull_cmd}` |\n")

        print(f"Markdown table written to {md_path}")


        # Write pull command
        os.makedirs(os.path.dirname(md_pull_path), exist_ok=True)
        with open(md_pull_path, "w") as f:

            # Sort by last_updated descending
            all_tags.sort(key=lambda t: t.get("last_updated", ""), reverse=True)

            for tag in all_tags:
                pull_cmd = f"docker pull {user}/{repo}:{name}"

                f.write(f"{pull_cmd}\n")
                break

        print(f"Markdown pull written to {md_pull_path}")

        # Write the docker image tag
        os.makedirs(os.path.dirname(md_image_path), exist_ok=True)
        with open(md_image_path, "w") as f:

            # Sort by last_updated descending
            all_tags.sort(key=lambda t: t.get("last_updated", ""), reverse=True)

            for tag in all_tags:
                image = f"{user}/{repo}:{name}"

                f.write(f"{image}\n")
                break

        print(f"Image tag written to {md_image_path}")
