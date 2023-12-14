from typing import List, Optional


def get_new_max_id(all_ids: List[int], id: Optional[int] = None) -> int:
    if not all_ids:
        if id:
            return id
        return 1
    if id and id not in all_ids:
        return id
    return max(all_ids) + 1
