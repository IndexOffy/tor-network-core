# tor-network-link

```
 _                        _                      _    
| |_ ___  _ __ _ __   ___| |___      _____  _ __| | __
| __/ _ \| '__| '_ \ / _ | __\ \ /\ / / _ \| '__| |/ /
| || (_) | |  | | | |  __| |_ \ V  V | (_) | |  |   < 
 \__\___/|_|  |_| |_|\___|\__| \_/\_/ \___/|_|  |_|\_\ v1.0
 ```

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
