🥾 **DropServe**: Street-Smart File Downloads for Open WebUI (or Any Docker Host)

[![Docker Build](https://img.shields.io/badge/build-docker-blue)](https://hub.docker.com/r/MattDGTL/dropserve)
### Quick Start
    
    ```bash
    docker run -d \
      --name dropserve \
      -p 8080:8000 \
      -v /your/host/folder:/webfiles \
      mattdgtl/dropserve

plug-and-play file server built for anyone running Open WebUI, LLM agents, or code tools in Docker that need a real, always-downloadable file link.
What is DropServe?
    DropServe is a dead-simple Docker container that hosts a folder and guarantees every file you (or your AI) create is downloadable by direct link—no browser drama, no MIME shenanigans, just pure “Save as…” every time.
    Built for Open WebUI, but works with any workflow, LLM, or automation needing a drop spot for files.

Why Would I Use This?
    Running Open WebUI (or any code-gen tool) in Docker? Want the AI to create files (scripts, zips, logs, reports) and instantly hand you a real, working download link?
    Want something more reliable than the built-in WebUI download logic or browser file handling?
    Need to share a folder with your homelab, team, or yourself—force-download every file, no matter the extension?

DropServe is the answer.
How Does It Work?
    Runs as a standalone Docker container.
    You map any folder you want to share as /webfiles.
    Open WebUI (or your own scripts/tools) write files to this mapped folder.
    Every file in there becomes instantly downloadable at
    http://your-server:8080/filename
    (with a “force download” header so your browser never tries to just display it).
    
How To Use With Open WebUI
    Map your Open WebUI outputs folder to DropServe’s /webfiles:
        If your Open WebUI is in Docker, set this in your docker-compose.yml:
    
    volumes:
      - /home/matt/docker/open-webui/outputs:/webfiles
      - /var/run/docker.sock:/var/run/docker.sock  # (Required for some Open WebUI tools)
This way, whenever your AI or code tool generates a file to /mnt/outputs (inside Open WebUI), it will appear in /webfiles inside DropServe.

    
Start DropServe:

    docker build -t dropserve .
    docker run -d -p 8080:8000 -v /home/matt/docker/open-webui/outputs:/webfiles dropserve

Get your download link:
    Any file written to /mnt/outputs (Open WebUI) or /webfiles (host/DropServe) will be downloadable at
    http://your-server:8080/yourfile.txt
    Files always download—no more browser “preview only” issues.

Open WebUI Integration Notes
    If you want Open WebUI to generate files you can download, make sure any tools or plugins write to the mapped /mnt/outputs directory.
    For some Open WebUI Docker setups (especially if using the DockerInterpreter tool), you also need:

    - /var/run/docker.sock:/var/run/docker.sock
in your Open WebUI Docker volumes for code execution features to work.

Features
    Force downloads. Every file, every time—no browser guesswork.
    Simple Docker deploy. No Python required on host.
    No files or scripts lost: Directory listing shows all files. Click = download.
    No permission games: As long as Docker can read your output folder, you’re set.

Example Setup

docker-compose snippet:

    services:
      openwebui:
        image: open-webui:latest
        volumes:
          - /home/matt/docker/open-webui/outputs:/mnt/outputs
          - /var/run/docker.sock:/var/run/docker.sock
        # other config...
    
      dropserve:
        build: .
        ports:
          - "8080:8000"
        volumes:
          - /home/matt/docker/open-webui/outputs:/webfiles

Shoutout

Built for the streets, tested in the lab—if your AI needs to hand you files, DropServe keeps the corner hot.
No more “I can’t download this” headaches.

