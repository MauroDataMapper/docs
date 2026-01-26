As well as the User Interface, you can also serve other static contents from within the container.
This is achieved by mounting the container with the volume that holds the static contents to serve.

From inside the container, static contents are served from within */home/app/resources/public/*

So, for example, if you have some contents to serve as yourhost.com/myui ,
and your contents are found at */path/to/myui/* , start the container with your contents bind mounted:

```bash
docker run \
...
-v /path/to/myui/:/home/app/resources/public/myui
...
```
