<h1 align="center">Machine Learning: Incremental Learning</h1>
<p>This repository consists of implementation and experiments that models hybrid machine learning algorithms using <code>K- Nearest Neighbor (KNN)</code> based <strong>incremental and concept drift</strong> techniques and aspects that informs the future discussions of new approaches towards integrating algorithms for forecasting and prediction.</p>

<h3 style="text-align:left"><span>Incremental Learning</span></h3>
<p dir="ltr">Incremental learning is a Machine Learning (ML) approach where models are updated continuously with new data without retraining from scratch. It is used both to handle large or streaming datasets that cannot fit into memory and to enable models to learn new information over time while minimizing catastrophic forgetting of previously learned knowledge.</p>

<h3 style="text-align:left"><span>Modelling the KNN classification distance measure</span></h3>
<p dir="ltr">In ideal circumstances, KNN works by finding distances between intersection of data by selecting
(𝑘) which is closest to the intersection point then votes for most frequent for classification or verge
the distances in regression.</p>

<p dir="ltr">KNN is implemented by;</p>

<ul>
<li> Selecting (𝑘) neighbors</li>
<li> Computing the (𝑘) number of neighbors (Euclidean distance)</li>
<li> Taking (𝑘) nearest neighbors as per the computed Eucleid distance</li>
<li> Computing the number if data points among (𝑘) neighbors</li>
<li> The new data points are then assigned to the maximum neighbor category</li>
</ul>

### Key Algorithm
<p><code>Algorithm 1: Determine maximum classification accuracy using corresponding 𝑘−𝑣𝑎𝑙𝑢𝑒𝑠 for distance metrics.
Input: Determine the datasets and class labels in the datasets as in the rate of 𝑥 𝑎𝑛𝑑 𝑦 respectively. Undertake the 𝑡𝑟𝑎𝑖𝑛 − 𝑡𝑒𝑠𝑡_𝑠𝑝𝑙𝑖𝑡𝑠 on 𝑥 𝑎𝑛𝑑 𝑦 and test the size "𝑡𝑒𝑠𝑡_𝑠𝑖𝑧𝑒" as a function of 𝛽. Assign the values corresponding to 𝑥𝑡𝑟𝑎𝑖𝑛 , 𝑥𝑡𝑒𝑠𝑡 , 𝑎𝑛𝑑 𝑦𝑡𝑒𝑠𝑡 .
Output: Max classification accuracy for determining the corresponding 𝑘−𝑣𝑎𝑙𝑢𝑒 for the distance metrics.
1: CLASSIFICATION_DISTANCE METRICS ={ Jaccard, Euclidean distance, Local Mean Euclidean, Chebyshevs, Hamming, Minkowski, Manhattan, Cosine }.
2: set MAX_DISTANCE_ACCURACY to an empty datasets dictionary.
3: for set of 𝐷 ∈ MAX_DISTANCE_METRICS do.
4:set of KNN_ACCURACY to an empty datasets dictionary
5:if K=3 to 13 perform step 2
6:for K=3 to 13 do;
7:KNN=Apply KNeigboursClassifiers (n_neigbours=k_metric=D);
8:KNN Score= KNN Model on 𝑥𝑡𝑟𝑎𝑖𝑛 , 𝑦𝑡𝑒𝑠𝑡 .
9: Enable K and determine
The conditions set for the datasets as follows;
KNN_CLASSIFIER_ACCURACY
MAX_ACCURACY as key value for the pair.
Table: Summary of datasets properties
10: end for.
</code></p>
