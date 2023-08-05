# Alias
A container system for private key management. Alias provides a framework which simplifies private key management. Container system for exchanges, wallets and APIs. This combination of modules enables a complete and flexible interface for any kind of parallel asset managmenet. 

Install
    
    pip install alias

Usage
    
    from alias import Alias
    
    a1 = Alias(                                # Assumes someID already has added keys
        identifier='someID' ,                  # Any name or identifier to access your vault
        private_key=channel.get('default') )   # Private key from message bus
    
    a1.stat()                                  # shows overview of current container state
    a1.scope()                                 # returns all capabilities within scope of container
    a1.vehicle('coinbase', 'BTC/USD')          # returns Vehicle() initialized with available credentials
    a1.all('BTC/USD')                          # returns all in-scope vehicles with BTC/USD capability
    
    
### Vehicle
A Vehicle is a TAC (Transactable Asset Container) for any kind of transactable asset. It abstracts the differences between exchanges, wallets, APIs, or shell protocols. Vehicles expose a broad range of functionality while hiding the inner workings and eliminating the differences between underlying assets. Vehicles can be used to store, access, move, and analyze all of your holdings simultanously. 

Usage
                                              
    x1 = a1.vehicle( ‘bittrex’ , ‘BTC/USD’ )   # Create a few random vehicle containers
    x2 = a1.vehicle( ‘coinbase’, ‘BTC/USD’ ) 
    x3 = a1.vehicle( ‘kraken’ , ‘ETH/USD’ )  
    
    x1.route( x3 )                             # finds cheapest route and moves all value to x3
    x1.collect( [ x2 , x3 , x4 ] )             # collect all value into x1
    x1.disperse( [ x2 , x4 ] )                 # disperse vall value accross x2, x4
    x1.transfer( x2 , 0.1 )                    # transfers 0.1 of base value to x2
    
    

Analytics Usage

    x1.mineTradebook()                          # Numpy / DataFrame with formatted tradebook + metadata
    x2.mineOrderbook()                          # Numpy / DataFrame with formatted orderbook + metadata
    x3.mineMetadata()                           # Extended metadata for vehicles asset


### Group
Provides a [concurrent.futures](https://docs.python.org/3/library/concurrent.futures.html) multiprocessing wrapper to enable fast and parallel execution of concurrent operations on all Vehicles and Aliases. Vehicle and Alias return matrices which are composable into aggregates using vectorized operations and available for asset and portfolio wide operations.

Usage
    from alias import Group

    g1 = Group( [x1,x2,x3] )
    g1.mineTradebook()                          # Concurrently Mine all Tradebooks 
    g1.mineOrderbook()                          # Concurrently Mine all Orderbooks
    

[ ] Add docs about group usage