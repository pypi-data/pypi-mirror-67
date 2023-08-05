from typing import List

from frater.data.category import Category
from .activity import Activity
from .activity_proposal import ActivityProposal

__all__ = ['activity_to_proposal', 'proposal_to_activity']


def proposal_to_activity(proposal: ActivityProposal, activity_type: Category = None,
                         confidence: float = 0.0, probabilities=None):
    """This function converts a proposal into an activity.

    :param ActivityProposal proposal: proposal for building new activity
    :param Category activity_type: activity type of the new activity
    :param float confidence: confidence of the activity
    :param List[float] probabilities: list of probabilities for the possible activity types
    :return: returns an :py:class:`~frater.core.activity.Activity` built from provided :py:class:`~frater.core.activity.ActivityProposal`
    :rtype: Activity

    """
    if probabilities is None:
        probabilities = []
    if activity_type is None:
        activity_type = Category(0, 'null', 'diva_activities')

    return Activity.init_from_activity_proposal(proposal, activity_type, confidence, probabilities)


def activity_to_proposal(activity: Activity) -> ActivityProposal:
    """This function converts an activity into a proposal


    :param Activity activity: activity to convert to proposal
    :return: the new activity proposal

    """
    return ActivityProposal(trajectory=activity.trajectory, objects=activity.objects,
                            source_video=activity.source_video, experiment=activity.experiment)
