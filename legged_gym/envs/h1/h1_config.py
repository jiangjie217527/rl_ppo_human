from legged_gym.envs.base.legged_robot_config import LeggedRobotCfg, LeggedRobotCfgPPO

class H1RoughCfg( LeggedRobotCfg ):
    class init_state( LeggedRobotCfg.init_state ):
        pos = [0.0, 0.0, 1.0] # x,y,z [m]
        default_joint_angles = { # = target angles [rad] when action = 0.0
           'left_hip_yaw_joint' : 0. ,
           'left_hip_roll_joint' : 0,
           'left_hip_pitch_joint' : -0.3,
           'left_knee_joint' : 0.7,
           'left_ankle_joint' : -0.4,
           'right_hip_yaw_joint' : 0.,
           'right_hip_roll_joint' : 0,
           'right_hip_pitch_joint' : -0.3,
           'right_knee_joint' : 0.7,
           'right_ankle_joint' : -0.4,
           'torso_joint' : 0.,
           'left_shoulder_pitch_joint' : 0.46,
           'left_shoulder_roll_joint' : 0,
           'left_shoulder_yaw_joint' : 0.,
           'left_elbow_joint'  : 0.,
           'right_shoulder_pitch_joint' : 0.46,
           'right_shoulder_roll_joint' : 0.0,
           'right_shoulder_yaw_joint' : 0.,
           'right_elbow_joint' : 0.,
        }


    class env(LeggedRobotCfg.env):
        num_observations = 69
        num_actions = 19


    class control( LeggedRobotCfg.control ):
        # PD Drive parameters:
        control_type = 'P'
          # PD Drive parameters:
        stiffness = {'hip_yaw': 300,
                     'hip_roll': 300,
                     'hip_pitch': 300,
                     'knee': 200,
                     'ankle': 40,
                     'torso': 300,
                     'shoulder': 150,
                     "elbow":50,
                     }  # [N*m/rad]
        damping = {  'hip_yaw': 3,
                     'hip_roll': 3,
                     'hip_pitch': 3,
                     'knee': 2,
                     'ankle': 1,
                     'torso': 5,
                     'shoulder': 2,
                     "elbow":1,
                     }  # [N*m/rad]  # [N*m*s/rad]
        # action scale: target angle = actionScale * action + defaultAngle
        action_scale = 0.02
        # decimation: Number of control action updates @ sim DT per policy DT
        decimation = 4

    class asset( LeggedRobotCfg.asset ):
        file = '{LEGGED_GYM_ROOT_DIR}/resources/robots/h1/urdf/h1.urdf'
        name = "h1"
        foot_name = "ankle"
        penalize_contacts_on = ["hip", "knee"]
        terminate_after_contacts_on = ["pelvis"]
        self_collisions = 1 # 1 to disable, 0 to enable...bitwise filter
        flip_visual_attachments = False

    class rewards( LeggedRobotCfg.rewards ):
        soft_dof_pos_limit = 0.9
        base_height_target = 0.98
        class scales( LeggedRobotCfg.rewards.scales ):
            tracking_lin_vel = 1.2
            tracking_ang_vel = 0.6
            lin_vel_z = -2.0
            ang_vel_xy = -1.0
            orientation = -1.0
            base_height = -100.0
            dof_acc = -3.5e-8
            feet_air_time = 1.0
            collision = 0.0
            action_rate = -0.01
            torques = 0.0
            dof_pos_limits = -10.0

class H1RoughCfgPPO( LeggedRobotCfgPPO ):
    class algorithm( LeggedRobotCfgPPO.algorithm ):
        entropy_coef = 0.01
    class runner( LeggedRobotCfgPPO.runner ):
        run_name = ''
        experiment_name = 'h1'
