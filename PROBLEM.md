Michal has too many passwords to remember, so he has decided to store some of them on his computer.
He realizes that storing passwords in plaintext is risky, so he decided to store only their hashes.
As a coding exercise, he implemented his own simple hash function.

What he forgot about is that one of the property of hash functions is that they are supposed to be one-way functions
meaning that the password can't be recovered from the hash. Now he needs to know his password, but
he only knows the stored hash. The only thing he remembers is that the password only contained
printable ASCII characters. Can you help him, or is his password lost forever?

The hash of his password, namely the output of `hash.py: my_hash()` function is:

`8b2ef66957b373ca383d71baa35d682b`

The answer is the recovered password.