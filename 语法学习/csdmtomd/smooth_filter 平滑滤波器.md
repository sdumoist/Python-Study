#./reasonyuanrobot/smooth_filter 平滑滤波器


### 1.移动平均法(邻域平均值滤波器)

One simple form of moving average is to calculate the average of adjacent measurements at a certain position. In a one-dimensional series of measurements a[1:N], for example, the moving average at a[n] can be calculated as a[n] = (a[n-1] + a[n] + a[n+1]) / 3, for example. If you go through all of your measurements, you're done. In this simple example, our averaging window has size 3. You can also use windows of different sizes, depending on how much smoothing you want

Use an algorithm based on convolution to make the calculation easier. The advantage of using convolution is that you can choose different kinds of averages, like weighted averages, by simply changing the window.

参考下面这个滤波器的实现：

```
bool SmoothingTrajectoryFilter::applyFilter(robot_trajectory::RobotTrajectory&amp; rob_trajectory) const
{
  /** 总体思路：
   * - 使用相邻的num_coef_个数据，来生成第i个数据过滤后的值 //num_coef_为奇数， k=num_coef_/2;  i-k,...,i,...,i+k 共2k+1个原始数据，num_coef_=2k+1
  * - 每个数据的比重(系数)，在coef_设定  //vector&lt;&gt;
  * - 每个数据，分别乘以coef_对应的系数，累加生成新值sum，除以增益gain_，作为第i个数据滤波后的值
  * 
  * e.g:
  *  sum = data(i-k)*coef_(i-k)+...+data(i)*coef_(i)+...data(i+k)*coef_(i+k);
  *  data_filter(i) = sum/gain_; //若gain_=num_coef_, coef_全为1，相当于取num_coef_个相邻数据的平均值
  * 
  */

  if(!initialized_) return(false);

  const int num_points = rob_trajectory.getWayPointCount(); 
  if(num_points &lt;=2) return(false); // nothing to do here, can't change either first or last point
  const int num_states = rob_trajectory.getWayPoint(0).getVariableCount();
  std::vector&lt;double&gt; xv;
    
  // filter each variable independently
  for(int i=0; i&lt;num_states; i++)
  { 
    double start_value     = rob_trajectory.getWayPoint(0).getVariablePosition(i);
    double start_slope     = rob_trajectory.getWayPoint(1).getVariablePosition(i) - start_value; // slope at start
    double end_value      = rob_trajectory.getWayPoint(num_points-1).getVariablePosition(i);
    double end_slope      = end_value - rob_trajectory.getWayPoint(num_points-2).getVariablePosition(i); // slope at end

    // initialize the filter to have initial slope
    xv.clear();
    double value = start_value - (num_coef_/2)*start_slope;
    for(int j=0; j&lt;num_coef_; j++) 
    { 
      xv.push_back(value);
      value += start_slope;
    }
    
    // cycle through every waypoint, and apply the filter, NOTE, 1st and last waypoints should not be changed
    for(int j=1; j&lt;num_points-1; j++)
    {
      // shift backwards
      for(int k=0; k&lt;num_coef_-1; k++)
      {
        xv[k] = xv[k+1];  
      }

      // get next input to filter which is num_coef/2 in front of current point being smoothed
      if(j+num_coef_/2 &lt; num_points)
      {	
        xv[num_coef_ - 1] = rob_trajectory.getWayPoint(j+num_coef_/2).getVariablePosition(i); // i'th state of j'th waypoint
      }
      else
      {
        end_value += end_slope;
        xv[num_coef_-1] = end_value; // fill by continuing with final slope
      }

      // apply the filter
      double sum = 0.0;
      for(int k=0; k&lt;num_coef_; k++)
      { 
        sum += xv[k]*coef_[k];
      }

      // save the results
      rob_trajectory.getWayPointPtr(j)-&gt;setVariablePosition(i,sum/gain_); // j'th waypoint, i'th variable set to output value

    }// end for every waypoint

  } // end for every state

  return(true);

}// end SmoothingTrajectoryFilter::applyfilter()
```

### 2.Savitzky-Golay S-G法

It uses least squares to regress a small window of your data onto a polynomial, then uses the polynomial to estimate the point in the center of the window. Finally the window is shifted forward by one data point and the process repeats. This continues until every point has been optimally adjusted relative to its neighbors.

是邻域平均值滤波器的改进，是基于最小二乘的卷积拟合算法，使用相邻2*k+1个数据的最小二乘拟合多项式，以此来计算第i个数据对应的滤波后的值。

Ｓ-Ｇ 滤波其实是一种移动窗口的加权平均算法，但是其加权系数不是简单的常数窗口，而是通过在滑动窗口内对给定高阶多项式的最小二乘拟合得出。 

Savitzky-Golay平滑滤波被广泛地运用于数据流平滑除噪，是一种在时域内基于局域多项式最小二乘法拟合的滤波方法。这种滤波器最大的特点在于在滤除噪声的同时可以确保信号的形状、宽度不变。  

**进一步参考**：







### 3.FFT滤波器



### 4. Gaussian Filter



### 5.Kalman Filter






