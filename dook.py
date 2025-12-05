# By Alex Pagac

# Install these dependices 
# none so far

# Dependincies ====----
# pip install google

# Modules ====---- 
from google import search

# Web Browser ====----
ip=raw_input("What would you like to search for? ")

for url in search(ip, stop=20):
     print(url)


# Art ====----
def art(): 
    """
    
  ____              _     
 |  _ \  ___   ___ | | __ 
 | | | |/ _ \ / _ \| |/ / 
 | |_| | (_) | (_) |   <  
 |____/ \___/ \___/|_|\_\ 
 
    by ShadeXplot

    
    """
print(art.__doc__)

