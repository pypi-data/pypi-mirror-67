# Ultru CLI
Use the Ultru<sup>TM</sup> CLI to easily access your data analytics. The CLI tool requires an API token that can be retrieved from the Ultru<sup>TM</sup> app page after logging with your credentials. The API token will be accessible in the form of a file that is either placed in the `current` directory, or in another directory, in which case the CLI can be pointed to the file using an argument switch.

## Accessing the API Key
![Retrieve an API KEY from the Ultru UI](docs/APIKEY.PNG)

## Using the CLI
The Ultru<sup>TM</sup> CLI tool has a helper screen that can be accessed by typing: `ultru-cli --help`.

Once the API key is downloaded, the `ultru-cli` tool can be executed from the same directory, without specifying the full path to the ultru.key. If the ultru.key is specified, specify an absolute or relative path.

There are currently two modes:
* Query By Type
* Query By Score

**By Type**
```bash
ultru-cli -e "demo" by-type -t user -o users.json -a
```
Will retrieve all users in the `demo` engagement

**By Score**
```bash
ultru-cli -e "demo" by-score -s benign -t process -o benign_processes.json -a
```
Will retrieve all processes in the `demo` engagement with a `benign` score.

**Other Arguments**
* `--count-only`: when specified, only returns the count of the selected records, versus the records themselves
* `--record-count`: when specified, will allow setting the number of records returned in a query
* `--get-all`: when specified, will retrieve all relevant records within the type and score constraints
