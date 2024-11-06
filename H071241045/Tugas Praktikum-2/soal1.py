{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "segitiga sama sisi\n"
     ]
    }
   ],
   "source": [
    "a = int(input(\"masukan panjang sisi a: \"))\n",
    "b = int(input(\"masukan panjang sisi b: \"))\n",
    "c = int(input(\"masukan panjang sisi c: \"))\n",
    "\n",
    "if a + b > c and a + c > b and b + c > a:\n",
    "    if a == b == c:\n",
    "        print(\"segitiga sama sisi\")\n",
    "    elif a == b or b == c or a == c:\n",
    "        print(\"segitiga sama kaki\")\n",
    "    else:\n",
    "        print(\"segitiga sembarang\")\n",
    "else:\n",
    "    print(\"tidak dapat membentuk segitiga yang valid\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
