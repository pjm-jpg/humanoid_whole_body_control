"""Whole Body Tracking termination presets for the H1 robot."""

from holosoma.config_types.termination import TerminationManagerCfg, TerminationTermCfg

h1_19dof_wbt_termination = TerminationManagerCfg(
    terms={
        "timeout": TerminationTermCfg(
            func="holosoma.managers.termination.terms.common:timeout_exceeded",
            is_timeout=True,
        ),
        "bad_tracking": TerminationTermCfg(
            func="holosoma.managers.termination.terms.wbt:BadTrackingZOnly",
            params={
                # robot tracking
                "bad_ref_pos_threshold": 0.5,
                "bad_ref_ori_threshold": 0.8,
                "bad_motion_body_pos_threshold": 0.25,
                # NOTE: body_names_to_track is shared with command_manager
                "body_names_to_track": [
                    "pelvis",
                    "left_hip_roll_link",
                    "left_knee_link",
                    "left_ankle_link",
                    "right_hip_roll_link",
                    "right_knee_link",
                    "right_ankle_link",
                    "torso_link",
                    "left_shoulder_roll_link",
                    "left_elbow_link",
                    "right_shoulder_roll_link",
                    "right_elbow_link",
                ],
                "bad_motion_body_pos_body_names": [
                    "left_ankle_link",
                    "right_ankle_link",
                ],
                # object tracking
                # only triggered when has_object=True
                "bad_object_pos_threshold": 0.25,
                "bad_object_ori_threshold": 0.8,
            },
        ),
    }
)

__all__ = ["h1_19dof_wbt_termination"]
