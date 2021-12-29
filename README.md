# RSA-thing

Hopefully y'all are rational enough to understand that this is just for 
exploration purposes and shouldn't actually used in any way.

## What is RSA
RSA is a cryptosystem that allows anybody to encrypt messages using a publicly 
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
        - since we know that *n* = *p * q*, φ(*n*) is just *(p-1)(q-1)*
        - now, we find *d*, which is the modular inverse of *e (mod* φ(*n*)*)*
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

Now, imagine you're a hacker and want to break RSA encryption. Say you get ahold of
*n*, *e*, and *c* which is *m<sup>e</sup> (mod n)*. It looks possible that we could
try and find the modular root *e* of *m* to get *m*, but because how moduluses loop 
around it turns into hell and long story short there is no efficient solution. So that approach fails.

**So to get *m* from *c*, our best approach is to get what *d* is.**

To get *d*, we need *e* and *φ(n)*. *e* is avaliable for free through the public key, 
and so is *n*, but to actually get φ(*n*) is a different story

φ(*n*) is Euler's totient function which is the number of positive integers below *n* that are 
relatively prime to *n*. In other words, if we just have *n* to find φ(*n*) we have to go through
every number below *n*, and check if they are relatively prime. 

This sounds doable but with our assumption that *p* and *q* are massive, 
*n* is going to be MASSIVE MASSIVE. There is no person or computer that can 
go through that process in a reasonable amount of time.

But, wait, we calculated φ(*n*) so easily! That's because if we know the prime factors
of *n*, in this case *p* and *q*, we can easily calculate φ(*n*) as *(p-1)(q-1)*. So RSA is broken 
then right? We have *n*, so all we have to do is factor *n* into *p* and *q*, and BAM we have 
φ(*n*) and then *d* and then we can decrypt all those messages.

Except that [integer factorization](https://en.wikipedia.org/wiki/Integer_factorization)
is actually a really tough problem in mathematics.
Especially when the only factors of a number are two primes and is 
giant in size, like *n*, once again despite the best efforts of mathematicians around the 
world, the task takes so long that there is no person or computer that can 
go through that process in a reasonable amount of time.

So if you keep your *p*, *q*, φ(*n*), and *d* secret, and only publish the public key, despite
the fact that it is technically always POSSIBLE to find the decryption key from *n* and *e*, 
there is no chance of it happening in reality due to the time needed.

Of course, human error tends to play a hand here, so if *p* and *q* aren't randomly selected
enough, if one of those crucial numbers leaks, or if you get with some BS like a 
timing attack, then a hacker can break the
encryption. 

It's also interesting to note that technically there IS a way to factor numbers efficiently, which like
we said would break RSA. The problem is that [the process](https://en.wikipedia.org/wiki/Shor%27s_algorithm)
needs a fucking QUANTUM computer. So it doesn't work on any real computer in
use today. With quantum computing being the absolute cutting edge of research right now and the largest
number successfully factored with that algorithm being 15 as of December 2021, RSA is still safe. But 
yeah, if quantum computing continue to develop successfully, eventually
RSA will be broken.

But in theory, this is why RSA is secure (for now)!

## Why the math works
The magic of the math behind RSA is related to modular arithmetic, especially modular
inverses.

To put the algorithm in a pure math sense, we start with a number *m*. <br />
We encrypt it with *m<sup>e</sup> (mod n)*, which gives us the number *c* <br /> 
We decrypt it with *c<sup>d</sup> (mod n)* which gives us *m* back. <br />
In other words with substitution, 
*(m<sup>e</sup>)<sup>d</sup>* ≡ *m<sup>ed</sup>* ≡ *m (mod n)*

To see why this works, **first let's consider the case where *m* and *n* are relatively prime.**
This isn't always true despite it being by far the most prevalent case for any given
*m* and *n*, but we will prove later that RSA still holds even when
*m* and *n* aren't relatively prime.

First, we'll use Euler's theorem, which is very related to Euler's totient function.
> Euler's theorem states that if *n* and *a* are positive coprime integers, then
> *a<sup>φ(*n*)</sup>* ≡ *1 (mod n)*, where φ(*n*) is our beloved Euler's totient function

Notice that with this fact, we can generalize a bit for what happens if the exponent is 
a multiple of φ(*n*)

For instance, a<sup>2φ(*n*)</sup> is the same as a<sup>φ(*n*)</sup> *
a<sup>φ(*n*)</sup>. Applying Euler's theorem to these individually gets us *1 * 1* ≡ *1* (mod n)
This logic applies to any multiple of φ(*n*)

So in a way, Euler's theorem holds for all multiples of φ(*n*). We can translate this
into a more general statement for Euler's theorem, like so
> if *n*, *b*, and *a* are positive integers and *n* and *a* are coprime, then if *b* ≡ *0* *(mod* φ(*n*)*)*,
> *a<sup>b</sup>* ≡ *1 (mod n)*, where φ(*n*) is our beloved totient function

Hopefully the wording isn't too confusing. All this is saying is that if *b*, our exponent,
is divisible by φ(*n*), aka *b* is a multiple of φ(*n*), then *a<sup>b</sup>* ≡ *1 (mod n)*,
the same conclusion we came to above.

Now before we actually get to how this relates to RSA, I want to just squeeze in 
a short realization. What happens if *b* ≡ *1* *(mod* φ(*n*)*)*? Well, all this does 
is tack on another *m* to be multiplied during the exponentiation. So all we do is 
multiply that extra *a* times 1, which is *a*. 
>So if *b* ≡ *1* *(mod* φ(*n*)*)*, then *a<sup>b</sup> ≡ a (mod n)*

>If you want a deeper explanation, note another way we can write *b* is 1 + *h*φ(*n*) 
> where *h* is some random integer by the definition of modular congruence. 
> So if we expand out the equation we get *a<sup>b</sup>* ≡ *a<sup>1+hφ(n)</sup>* , 
> which is congruent to *a<sup>1</sup>* * 
> *a<sup>hφ(n)</sup>* ≡ *a * 1* ≡ *a (mod n)*.

Alright, now how this relates to RSA. Once we've come this far it's pretty simple.
Recall that we found *d* to be the modular inverse of *e (mod* φ(*n*)*)*, so
*de* ≡ *1 (mod* φ(*n*)*)*. And we have our context that we are calculating
*m<sup>de</sup>  (mod n)*. So since *de* is our exponent, directly applying the 
ideas we found earlier gets us that *m<sup>de</sup> ≡ m (mod n)*

### Cases where *m* and *n* aren't relatively prime:

Alright, so in this case, either *p* or *q* divides *m*. We can break this into 2 more subcases:

**Both *p* and *q* divide *m***:

This means that *n* divides *m*, because *n* = *pq*. In other words, *m* ≡ *0 (mod n)*. Hopefully you can
see that raising *m* to the *e*-th power just gives us *m*<sup>*e*</sup> ≡ *0 (mod n)* again. The same
applies to *m*<sup>*de*</sup>, so *m*<sup>*de*</sup> ≡ *0* ≡ *m (mod n)*, exactly what we want.

**Only one of *p* or *q* divides m**:

Let's just assume without loss of generality that *p* divides *m* and *q* doesn't, since the reverse proof in the 
case that *m* divides and *p* doesn't would be exactly the same. Our basic proof idea here will to be to show that
*m*<sup>*de*</sup> ≡ *m (mod p)* and *m*<sup>*de*</sup> ≡ *m (mod q)* hold, which implies our
result *m*<sup>*de*</sup> ≡ *m (mod n)*

So we have *m* ≡ *0 (mod p)* and *m* /≡ *0 (mod q)* <sup>(that weird /≡ means not congruent to, idk how to use the actual
symbol)</sup>. Note here that we have that *m* is relatively prime to *q*. Sounds familiar? We already proved that RSA holds
for *m* and *n* if they are relatively prime. As it turns out, this logic extends to this case as well. So we already have that
*m*<sup>*de*</sup> ≡ *m (mod q)*

So now that all we need is to prove the case where *p* divides *m*. Once again, sound familiar? Yup, this our logic for when
*n* divides *m* holds here as well. So we get *m*<sup>*de*</sup> ≡ *0* ≡ *m (mod p)*, and all together we have 
*m*<sup>*de*</sup> ≡ *m (mod n)* for all cases. 

## Final thoughts
It's honestly amazing how the math all checks out AND the encryption is tough to break. Holy fuck.
Yeah that's all, how did they come up with this.
