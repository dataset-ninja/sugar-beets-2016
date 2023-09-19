The authors of the **Sugar Beets 2016** dataset present a substantial agricultural robot dataset focusing on plant classification, as well as localization and mapping, to support the growing interest in agricultural robotics and precision farming. The dataset encompasses various growth stages of plants, which are vital for tasks such as robotic intervention and weed control. The data collection took place over three months in the spring of 2016 on a sugar beet farm near Bonn, Germany, utilizing a commercially available agricultural field robot.

<img src="https://github.com/dataset-ninja/pascal-voc-2012/assets/78355358/28474d1f-d909-49d1-a261-5d63ceda6747" alt="image" width="800">

Throughout this period, data was recorded approximately three times a week, commencing at plant emergence and concluding when the field became inaccessible to machinery without damaging the crops. The agricultural robot used was equipped with a four-channel multi-spectral camera, an RGB-D sensor, multiple lidar and global positioning system (GPS) sensors, as well as wheel encoders, all of which were calibrated before data acquisition. Additionally, lidar data of the field captured with a terrestrial laser scanner is included.

The dataset aims to assist researchers in the development of autonomous systems designed for operating in agricultural field environments. It offers real-world data for tasks like plant classification, navigation, and mapping. The data encompasses visual plant information, navigation-related measurements, and intrinsic/extrinsic calibration parameters for all sensors, along with Python-based development tools for data manipulation.

The agricultural robot used for data collection is the BoniRob platform, a versatile robot developed by Bosch DeepField Robotics for precision agriculture applications, including mechanical weed control, herbicide spraying, and plant and soil monitoring. BoniRob boasts four independently steerable wheels, enabling flexible movements on rough terrain.

Regarding the sensor setup, the BoniRob platform features multiple sensors:

1. **JAI AD-130GE Camera**: This multi-spectral vision sensor provides image data in three RGB bands and one near-infrared (NIR) band. The NIR channel is valuable for distinguishing vegetation from soil and other background elements.
2. **Kinect One (Kinect v2)**: This time-of-flight camera by Microsoft provides RGB and depth information, with pixels corresponding to create 3D point clouds.
3. **Velodyne VLP16 Puck**: A 3D lidar sensor with 16 laser diodes, offering distance and reflectance measurements. It's crucial for 3D mapping, localization, and obstacle detection.
4. **Nippon Signal FX8**: This 3D laser range sensor provides distance measurements up to 15 meters, with applications in obstacle avoidance and plant row detection during field navigation.
5. **Leica RTK GPS**: For precise position tracking, employing a Real-Time Kinematic (RTK) GPS system that provides centimeter-level accuracy.
6. **Ublox GPS**: A low-cost GPS receiver that uses Precise Point Positioning (PPP) for position estimation.

The data acquisition campaign spanned two months, covering various growth stages of sugar beet plants. Data was collected on an average of two to three days per week, resulting in approximately 5 TB of uncompressed data. This data includes high-resolution plant images, depth information from the Kinect, 3D point clouds from lidar scanners, GPS positions, and wheel odometry. The collection was strategically timed to capture key variations in the field relevant to weed control and crop management, covering various weather and soil conditions.

Furthermore, the authors have provided ground truth data for plant classification, which includes labeled images distinguishing sugar beets and multiple weed species.

The dataset and its associated sensor setup are expected to support the development of autonomous agricultural robot systems, helping advance precision farming and weed control practices.

<i>Note, that the present dataset contains only the **nir** and **rgb** information from JAI camera. Follow to the original page to grab the data from other sensors.</i>
