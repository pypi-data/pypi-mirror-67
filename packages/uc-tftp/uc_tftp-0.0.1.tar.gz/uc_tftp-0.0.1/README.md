# uc_tftp  
Implementation of classes and functions for working with files via tftp.  

It is part of the Unicon project.

https://unicon.10k.me

## Usage:

##### Install
```sh
pip install --user uc-tftp
```
##### and use

```python
from uc_tftp import TFTPReceiver
```

## Examples:  
**as iterator**  

```python
receiver = TFTPReceiver(timeout=3)  
for data in receiver:  
	print(data)  
```

**as function**  

```python
receiver = TFTPReceiver(timeout=3)  
receiver.recvto("/path/to/destination")  
```

**with filename**

```python
receiver = TFTPReceiver(timeout=3)  
receiver.open()  
with open(receiver.filename, "w") as file:  
    for block in receiver:  
        file.write(block)  
```

## Exceptions  
May raise exceptions in the following cases:  

**NoWRQPacket**  

If the connected client tried to perform a non-WRQ operation (data recording).  

**NoIncomingConnection**  

If there were no connections in the allotted time.  

**ErrorReceived**  

If error packet was received from client.  

**UnexpectedOpcode**

If an unexpected opcode is received during data transfer.
