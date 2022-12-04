# tor-network-link

## Running the project with [Docker]

 - Building the Docker image

```bash
$ sudo docker build --tag tor-link --file docker/Dockerfile .
$ sudo docker build --tag tor-link --file docker/Dockerfile.chrome .
$ sudo docker build --tag tor-link --file docker/Dockerfile.tor .
```

 - Starting the Docker Container

```bash
$ sudo docker run -d -t tor-link
```

 - Enter the container

```bash
$ sudo docker exec -i -t ID /bin/bash
```

## Commands [Docker]

```dockerfile
CMD ["python", "source/main.py", "chrome", "--run", "explore_page"]
CMD ["python", "source/main.py", "chrome", "--run", "search_page"]
```


### Commit Style
- ⚙️ NO-TASK
- 📝 PEP8
- 📌 ISSUE
- 🪲 BUG
- 📘 DOCS
- 📦 PyPI

**RESOURCES**
- GitHub: https://github.com/IndexOffy/tor-network-link
- Docs:   http://www.indexoffy.com/
