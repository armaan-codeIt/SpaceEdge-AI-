from dataclasses import dataclass
from enum import Enum
class ActionType(str,Enum):
    TRANSMIT_RAW="TRANSMIT RAW"
    TRANSMIT_COMPRESSED= "TRANSMIT COMPRESSED"
    DEFER= "DEFER"
    @dataclass
    
    class Observation:
        id: str
        name: str
        event_type: str
        raw_size: float
        base_urgency: float
        confidence : float
        deadline_hours: float
        age_ticks: int = 0
        compression_ratio: float=0.30
@property
def compressed_size_mb(self)->float:
    return round(self.raw_size_mb* self.compression_ratio,1)
    
@dataclass
class SatteliteState:
    bandwidth_window_mb: float= 100.0
    battery_level_perc: float= 85.0
    solar_charging: bool= False
    orbit_pass_number: int = 1
        
@dataclass
class ScheduleDecision:
    task: Observation
    action: ActionType
    allocated_size_mb: float
    calculated_utility: float
    efficiency_ratio: float
    explanation: str
    
    