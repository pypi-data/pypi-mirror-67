This is the official python (websocket) repo for TrueData.
-------


**What have we covered so far ?**
* Websocket APIs
  *  Live data
  *  Historical data

**How do you use it ?**

**For beginners**

* Installing from PyPi
```shell script
python3.7 -m pip install truedata
```

* Connecting 
```python
from truedata_ws.websocket.TD import TD
td_app = TD('<enter_your_login_id>', '<enter_your_password>')
```

* Starting live data
<br>For Single Symbols
```python
req_id = td_app.start_live_data('<enter_symbol>')
# Example:
# req_id = start_live_data('CRUDEOIL-I')
# This returns an integer that can be used later to reference the data
```
For Multiple symbols
```python
req_ids = td_app.start_live_data(['<symbol_1>', '<symbol_2>', '<symbol_3>', ...])
# Example:
# req_ids = td_app.start_live_data(['CRUDEOIL-I', 'BANKNIFTY-I', 'RELIANCE', 'ITC'])
# This returns a list that can be used to reference data later
```

* Sample code for testing market data (single symbol)
```python
from copy import deepcopy

live_data_obj = deepcopy(td_app.live_data[req_id])

while True:
    if not td_app.live_data[req_id] == live_data_obj:
        print(td_app.live_data[req_id])
        live_data_obj = deepcopy(td_app.live_data[req_id])
```

* Sample code for testing market data (multiple symbols)
```python
from copy import deepcopy

live_data_objs = {}
for req_id in req_ids:
    live_data_objs[req_id] = deepcopy(td_app.live_data[req_id])
    print(live_data_objs[req_id])

while True:
    for req_id in req_ids:
        if not td_app.live_data[req_id] == live_data_objs[req_id]:
            print(td_app.live_data[req_id])
            live_data_objs[req_id] = deepcopy(td_app.live_data[req_id])
```
<br>
<br>
<br>
<br>
<br>
<br>

<!---
**For advanced users**
* Installing from PyPi
```shell script
python -m pip install truedata==xx.xx.xx # Pick your version number from available versions on PyPi
```
* Installing from source

Download the sources

Make "truedata" the working directory using cd
```
python3 setup.py install
```

* Connecting 
```
from truedata.websocket.TD import TD
td_app = TD('<enter_your_login_id>', '<enter_your_password>, live_port=8080, historical_port=8090)  # historical_port should be None, if you do not have access to historical data...
```

* Starting live data
```
td_app.start_live_data('<enter_symbol>', req_id=2000)  # Example: td_app.start_live_data('CRUDEOIL-I')
count = 0
while count < 60:
    print(td_app.live_data[2000].__dict__)
    sleep(1)
    count = count + 1
```
-->
  
**What is the plan going forward ?**
* Ease of contract handling
* Improved error handling
