# Pokemon Type Fetcher
## Communication Contract

### Microservice Instructions
**Requesting data from microservice:**
To request data from the microservice, write the name of the pokemon preceded by a `$` to the CSV file `typereq.csv`. This CSV file must be created prior to running the microservice.

An example call for the Pokemon Goomy would be `$goomy` written to `typereq.csv`, with no trailing newlines or spaces after the name, This service matches for Pokemon by exact name, so partial matches will not return a type, though capitalization does not matter.

**Receiving data from microservice:**
The microservice will write the type of the pokemon to the same CSV file `typereq.csv`. If the first character is no longer a `$` sign, the microservice has successfully read and returned a result to the file. All results will come in a comma-separated value (CSV) format, with no spaces in between each type. The types will be capitalized.

An example of return data for the Pokemon Ribombee would be `Bug,Fairy`, written to `typereq.csv` by the microservice.

### UML Sequence Diagram:
![UML diagram for microservice.](https://i.imgur.com/kJdyPvh.png)