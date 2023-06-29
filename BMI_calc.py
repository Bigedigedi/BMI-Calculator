{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "mathematical-pillow",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Please give your size in cm 185\n",
      "Please give your weight in kg 95\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Your BMI is 27.8 .You are overweight\n"
     ]
    }
   ],
   "source": [
    "size = float(input(\"Please give your size in cm\"))\n",
    "weight = float(input(\"Please give your weight in kg\"))\n",
    "\n",
    "def bmi_calc(size,weight):\n",
    "    size_in_m = size/100\n",
    "    bmi = weight/(size_in_m**2)\n",
    "    \n",
    "    if bmi < 18.5:\n",
    "        print(\"Your BMI is\",round(bmi,1),\".You are Underweight\")\n",
    "    elif bmi < 25:\n",
    "        print(\"Your BMI is\",round(bmi,1),\".You are normalweight\")\n",
    "    elif bmi < 30:\n",
    "        print(\"Your BMI is\",round(bmi,1),\".You are overweight\")\n",
    "    else:\n",
    "        print(\"Your BMI is\",round(bmi,1),\".You have adipositas\")\n",
    "\n",
    "bmi_calc(size,weight)"
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
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
