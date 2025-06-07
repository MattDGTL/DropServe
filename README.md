# 🥾 DropServe: Files On The Corner

Ain’t no cloud, ain’t no waiting—DropServe turns any folder into a block party for your files.  
Whatever you or your AI cook up, DropServe gives you a dead-simple download link—no questions asked, no browser drama.

- **Always force-downloads.** Text, zips, logs, you name it—every file drops like a mixtape in 2003.
- **Bulletproof Docker build.** No Alpine headaches, just works.
- **Plug and play with Open WebUI, your homelab, or anything with files to share.**

*Built with NYC hustle, tested by the streets, approved by Timbs.*

---

## Quick Start

```bash
docker build -t dropserve .
docker run -d \
  --name dropserve \
  -p 8080:8000 \
  -v /host/folder/with/files:/webfiles \
  dropserve
