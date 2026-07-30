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
