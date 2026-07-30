<h1 align="center">Machine Learning: Incremental Learning</h1>
<p>This repository consists of implementation and experiments that models hybrid machine learning algorithms using <code>K- Nearest Neighbor (KNN)</code> based <strong>incremental and concept drift</strong> techniques and aspects that informs the future discussions of new approaches towards integrating algorithms for forecasting and prediction.</p>

<ul>
<li> Selecting (𝑘) neighbors</li>
<li> Computing the (𝑘) number of neighbors (Euclidean distance)</li>
<li> Taking (𝑘) nearest neighbors as per the computed Eucleid distance</li>
<li> Computing the number if data points among (𝑘) neighbors</li>
<li> The new data points are then assigned to the maximum neighbor category</li>
</ul>

<h3 style="text-align:left"><span>1. Euclidean Distance</span></h3><p dir="ltr"><span>Euclidean distance is defined as the straight-line distance between two points in a plane or space. You can think of it like the shortest path you would walk if you were to go directly from one point to another.</span></p><blockquote><p dir="ltr">d( x, X_i ) = sqrt{sum_{j=1}^{n} ( x_j - X_{ij} )^2}</p></blockquote>
