##### Description
1. *src* - source module:
      1. *parser-module* stands for all scripts
      2. *parser-libraries* stands for:
         1. *SQL* - *mySQL_save* function that saves info to the temporary table, and migrates it to the original one.
         2. *functions* - bundle of functions which are used in parser-module
         3. *openpy* - function to save people into EXCEL file
2. *parser-main* is the main module that can be installed with:
    ```sh
    $ sudo pip3 install parser-main (-U if the 3.0 version has been already installed)
    ```
	Then you can run it:
	```sh
	$ python -m parser-main
	```
3. You should also do 
   ```sh
    $ sudo pip3 uninstall parser-module 
    $ sudo pip3 uninstall ParSer_Libraries
   ```
   if the *parser-main.3.0* has been already installed.
4. config.txt is the settings file for the DB. You shold put the connection information there.