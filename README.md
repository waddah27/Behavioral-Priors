The primary goal of this study is to acquire, process, and encode trajectory and interaction data pertinent to the execution of contact-rich tasks, 
specifically focusing on the intricate task of cutting. This entails capturing both kinematic and dynamic information during the cutting process to form behavior priors, 
serving as foundational knowledge for Learning from Demonstration (LfD) or Skill Learning (SKL) models in robotic systems.

  **1. Data Collection**
  * **Trajectory Data**: Capture high-resolution trajectory data that encom-
passes the movement, orientation, and position of the cutting tool (e.g.,
robotic arm, knife) during cutting actions.
* **Interaction Data**: Gather force and torque information exerted on the
tool or workpiece to characterize the contact forces and dynamic inter-
actions occurring during cutting maneuvers.

**2. Data Treatment**:
• **Alignment and Synchronization**: Ensure synchronization between
trajectory and interaction data to create coherent sequences representa-
tive of the cutting actions.
• **Preprocessing**: Apply noise reduction, filtering, and normalization tech-
niques to enhance data quality and consistency, ensuring robustness in
subsequent processing steps.
3. **Encoding Behavior Priors**:
• Feature Extraction: Derive salient features from the aligned trajectory
and interaction data, potentially including tool pose variations, force
distributions, and contact event sequences specific to cutting actions.

* **Gaussian Mixture Models (GMM)**: Utilize GMM to model the joint
distribution of these extracted features, capturing the nuanced variations
and patterns inherent in cutting tasks.
• **Gaussian Mixture Regression (GMR)**: Employ GMR to perform
regression within the GMM components, facilitating the mapping from
observed features to desired actions or behaviors during cutting.
