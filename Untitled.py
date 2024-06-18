{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "aebfc745-0a1d-4633-8a56-b3dffd33f897",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Minimum mesafe: 2.23606797749979\n"
     ]
    }
   ],
   "source": [
    "import math\n",
    "#Noktaları tanımlayalım.\n",
    "\n",
    "points = [(0, 0), (1, 2),(-3,-1),(2,4), (4,5), (9, 15)]\n",
    "\n",
    "#Öklid Mesafesi için fonksiyon yazalım.\n",
    "\n",
    "def euclideanDistance(point1,point2):\n",
    "    x1,y1=point1\n",
    "    x2,y2=point2\n",
    "    return math.sqrt((x2-x1)**2+(y2-y1)**2)\n",
    "\n",
    "#Mesafeleri hesaplayalım.Bunun için bir distances adında bir list oluşturalım.\n",
    "\n",
    "distances=[]\n",
    "for i in range(len(points)):\n",
    "     for j in range(i + 1, len(point\n",
    "                               s)):\n",
    "        distance = euclideanDistance(points[i], points[j])\n",
    "        distances.append(distance)\n",
    "\n",
    "#Minimum mesafeyi bulalım.\n",
    "\n",
    "minimum_distance=min(distances)\n",
    "print(\"Minimum mesafe:\",minimum_distance)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "706e5e24-a397-4fa3-8c6e-693643d8ef1d",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
