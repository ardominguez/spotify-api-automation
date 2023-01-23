# spotify-api-automation
Automation testing api framework for Spotify api

## Getting Started

Clone charmandeer-qa repository and install requirements. It's
highly recommendable to use a virtualenv.


```bash
git clone https://github.com/ardominguez/spotify-api-automation.git
cd spotify-api-automation
```

Create a Virtualenv in root path and activate

```bash
python3 -m venv behave
source behave/bin/activate
```

Install requirements
```bash
pip3 install -r requirements.txt
```
## Configure global viariable

- CLIENT_ID
- CLIENT_SECRET
- REFRESH_TOKEN


## Running Tests

To run a single test case (scenario):

```bash
behave -n "Test case name"
```
    
To run a feature file:

```bash
behave  features/name.feature
```
    
To run multiple features files:

```bash
behave  "feature name 1.feature" "feature name 2.feature"
```
