(import [math [sqrt]]
         [typing [List Union]])

(require [hy.contrib.destructure [fn+]])


(setv NumberList (of List (of Union int float)))


(defn ^float average [^NumberList xs]
   "Calculates an arithmetic average."
   (/ (sum xs) (len xs)))


(defn ^float variance [^NumberList xs]
   "Calculates a variance."
   (setv ^float avg (average xs))
   (/ (sum (map (fn [x] (** (- x avg) 2)) xs)) (len xs)))


(defn ^float standard-deviation [^NumberList xs]
   "Calculates standard deviation"
   (->> xs
        (variance)
        (sqrt)))


(defn ^float coefficient-of-variation [^NumberList xs]
   "Calculates coefficient of variation."
   (/ (standard-deviation xs) (average xs)))


(defn ^float covariance [^NumberList xs ^NumberList ys]
   "Calculates covariance of two vectors."
   (setv x-avg    (average xs)
         y-avg    (average ys)
        pairs-data     (zip xs ys)
        distance (fn+ [[x y]] (* (- x x-avg) (- y y-avg))))
   (/ (sum (map distance pairs-data)) (len xs)))


(defn ^float pearson-correlation-coefficient [^NumberList xs ^NumberList
ys]
   "Calculates Pearson linear correlation coefficient."
   (/ (covariance xs ys) (* (variance xs) (variance ys))))
