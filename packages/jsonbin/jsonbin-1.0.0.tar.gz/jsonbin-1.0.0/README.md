# jsonbin-client

## Installation
    pip install jsonbin-client

## Usage
    import jsonbin

    client = jsonbin.Client("YOUR_TOKEN_HERE") # use jsonbin.generate() or custom token

    client.store("key", "hello world") # supports any data type - including raw binary data

    client.retrieve("key") # returns "hello world"

    client.delete("key")

