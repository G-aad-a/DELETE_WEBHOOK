import requests
import time

def main():
    webhook = input("Webhook to Delete:")
    x = requests.delete(webhook)

   

if(__name__ == '__main__'):
    main()