# RSA-thing

Hopefully y'all are rational enough to understand that this is just for 
exploration purposes and shouldn't actually used in any way.

## What is RSA
RSA is a cryptosystem that allows anybody to encrypt messages using a publically 
avaliable key but can only be DECRYPTED by the key's publisher with a private key

The exact algorithm is detailed at [this wikipedia link](https://simple.wikipedia.org/wiki/RSA_algorithm)

Note for the nerds, my thing uses the Euler's totient function as detailed in the 
original paper, not the Carmichael's totient function that people actually use.

## A Dumb Explanation
Basically, RSA works like this:
1. we generate a public key-pair, *n* and *e*
    - *n* is the product of two primes, let's call them *p* and *q*
    - *e* is usually chosen to be 65537, which is prime and 2<sup>16</sup> + 1

2. we generate a private key, *d*
    - first, we need to calculate Euler's totient function (φ) on *n*
        - since we know that *n* = *p * q*, *φ(n)* is just *(p-1)(q-1)*
        - now, we find *d*, which is the modular inverse of *e (mod φ(n))*
            - because *e* is prime, we know that a modular inverse exists

Now, we encrypt a message by converting it to a number, call it *m*, and then 
our encrypted message is a number equal to

*m<sup>e</sup> (mod n)*, call this number *c*

We get *n* and *e* from the public key that is open for everybody to see and use

Now, from *c* we can actually get *m* right back just by

*c<sup>d</sup> (mod n)*, which just surprisingly equals *m*!

## Why is this secure?
First of all, RSA in practice requires that our two primes *p* and *q* be randomly choosen 
and be MASSIVE. You'll see why soon.

To get *m* from *c*, we have to know what *d* is. If we brute-force random numbers 
all we get is random gibberish numbers translating to random gibberish messages 
which isn't helpful.

To get *d*, we need *e* and *φ(n)*. *e* is avaliable for free through the public key, 
and so is *n*, but to actually get *φ(n)* is a different story

*φ(n)* is Euler's totient function which is the number of positive integers below *n* that are 
relatively prime to *n*. In other words, if we just have *n* to find *φ(n)* we have to go through
every number below *n*, and check if they are relatively prime. 

This sounds doable but with our assumption that *p* and *q* are massive, 
*n* is going to be MASSIVE MASSIVE. There is no person or computer that can 
go through that process in a reasonable amount of time.

But, wait, we calculated *φ(n)* so easily! That's because if we know the prime factors
of *n*, in this case *p* and *q*, we can easily calculate *φ(n)* as *(p-1)(q-1)*. So RSA is broken 
then right? We have *n*, so all we have to do is factor *n* into *p* and *q*, and BAM we have 
*φ(n)* and then *d* and then we can decrypt all those messages.

Except that integer factorization is actually a really tough problem in mathematics.
Especially when the only factors of a number are two primes and is 
giant in size, like *n*, once again despite the best efforts of mathematicians around the 
world, the task takes so long that there is no person or computer that can 
go through that process in a reasonable amount of time.

So if you keep your *p*, *q*, *φ(n)*, and *d* secret, and only publish the public key, despite
the fact that it is technically always POSSIBLE to find the decryption key from *n* and *e*, 
there is no chance of it happening in reality due to the time needed.

Of course, human error tends to play a hand here, so if *p* and *q* aren't randomly selected
enough or if one of those crucial numbers leaks, then a hacker can break the
encryption. But in theory, this is why RSA is secure.

## Why the math works
TODO LOL