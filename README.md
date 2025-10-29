To build the docker image:

```bash
docker build -t ror-records-ldes-builder .
```

To run:

```bash
docker run --rm -v "$(pwd)/your_input_folder:/workspace" ror-records-ldes-builder
```

for windows users
```bash
docker run --rm -v /$(pwd)/your_input_folder:/workspace ror-records-ldes-builder
```

