# mdb

A client to [my database](https://db.marcusweinberger.repl.co)

## Installation
    pip install marcusdb

Sorry, `mdb` was taken

## Usage
    import mdb

    keys = mdb.generate()
    # {"priv":"XXXXXXXX", "pub":"XXXXXXXXX"}
    # tip: the public key is just a hashed version of the private key [sha256(sha256(key) + salt)]

    privclient = mdb.Client(keys['priv'])
    pubclient = mdb.Client(keys['pub'])
    # yep, both use the same class. attempting priv methods with pub keys just dont work

    privclient.store("hello", "world")
    # can store all types of data by using the jsonpickle library

    pubclient.retrieve("hello")
    # > "world"

    pubclient.store("test", "wa")
    # will return False

    privclient.delete("hello")
    # returns True

    privclient.unregister(conf=True)
    # conf defaults to false, when false will do nothing
    # deletes your account from the DB, making both keys invalid and out of the system

## Github: [https://github.com/AgeOfMarcus/mdb](https://github.com/AgeOfMarcus/mdb)