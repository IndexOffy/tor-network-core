# tor-network-core

```
████████╗ ██████╗ ██████╗       ███╗   ██╗███████╗████████╗██╗    ██╗ ██████╗ ██████╗ ██╗  ██╗
╚══██╔══╝██╔═══██╗██╔══██╗      ████╗  ██║██╔════╝╚══██╔══╝██║    ██║██╔═══██╗██╔══██╗██║ ██╔╝
   ██║   ██║   ██║██████╔╝█████╗██╔██╗ ██║█████╗     ██║   ██║ █╗ ██║██║   ██║██████╔╝█████╔╝ 
   ██║   ██║   ██║██╔══██╗╚════╝██║╚██╗██║██╔══╝     ██║   ██║███╗██║██║   ██║██╔══██╗██╔═██╗ 
   ██║   ╚██████╔╝██║  ██║      ██║ ╚████║███████╗   ██║   ╚███╔███╔╝╚██████╔╝██║  ██║██║  ██╗
   ╚═╝    ╚═════╝ ╚═╝  ╚═╝      ╚═╝  ╚═══╝╚══════╝   ╚═╝    ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝
 ```

### Running the project with [Docker]

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

### Commands [Docker]

```dockerfile
CMD ["python", "source/main.py", "chrome", "--run", "explore_page"]
CMD ["python", "source/main.py", "chrome", "--run", "search_page"]
```

## Commit Style

- ⚙️ FEATURE
- 📝 PEP8
- 📌 ISSUE
- 🪲 BUG
- 📘 DOCS
- 📦 PyPI
- ❤️️ TEST
- ⬆️ CI/CD
- ⚠️ SECURITY

## License

This project is licensed under the terms of the GPL-3.0 license.

**RESOURCES**
- GitHub: https://github.com/IndexOffy/tor-network-link
- Docs:   http://www.indexoffy.com/
