<h1 align="center">Machine Learning: Incremental Learning</h1>
<p>This repository consists of implementation and experiments that models hybrid machine learning algorithms using <code>K- Nearest Neighbor (KNN)</code> based <strong>incremental and concept drift</strong> techniques and aspects that informs the future discussions of new approaches towards integrating algorithms for forecasting and prediction.</p>

<h3 style="text-align:left"><span>Incremental learning</span></h3>
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

<h3 style="text-align:left"><span>1. Euclidean Distance</span></h3><p dir="ltr"><span>Euclidean distance is defined as the straight-line distance between two points in a plane or space. You can think of it like the shortest path you would walk if you were to go directly from one point to another.</span></p><blockquote><p dir="ltr">d( x, X_i ) = sqrt{sum_{j=1}^{n} ( x_j - X_{ij} )^2}</p></blockquote>
