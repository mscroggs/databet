import sys

import github

access_key = sys.argv[-1]

git = github.Github(access_key)

databet = git.get_repo("mscroggs/databet")
branch = databet.get_branch("main")
ref = databet.get_git_ref("heads/main")
base_tree = databet.get_git_tree(branch.commit.sha)

vfile1 = databet.get_contents("VERSION", branch.commit.sha)
version = vfile1.decoded_content.decode("utf8").strip()

for release in databet.get_releases():
    if release.tag_name == f"v{version}":
        break
else:
    databet.create_git_tag_and_release(
        f"v{version}", f"Version {version}", f"Version {version}", "",
        branch.commit.sha, "commit")
