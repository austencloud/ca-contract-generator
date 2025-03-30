# models/contract.py
import json
import datetime
from dataclasses import dataclass, field, asdict


@dataclass
class Client:
    """Client information data class"""

    name: str = ""
    phone: str = ""
    email: str = ""
    title: str = ""


@dataclass
class Producer:
    """Producer information data class"""

    name: str = ""
    company: str = ""
    phone: str = ""
    email: str = ""


@dataclass
class Event:
    """Event information data class"""

    location: str = ""
    date: str = ""


@dataclass
class Fees:
    """Fee information data class"""

    total_fee: float = 250.0
    requires_deposit: bool = True
    deposit_amount: float = 125.0
    balance: float = 125.0
    payment_methods: str = "Business check, cash, Venmo, or Zelle."
    payment_terms: str = (
        "A non-refundable deposit is required within 48 hours of signing.\n"
        "Remaining balance is due immediately upon completion of the performance.\n"
        "Payment may also be made in advance.\n"
        "'Completion' is defined as the end of the performance or the moment the "
        "Performer ceases performing due to unforeseen circumstances. Full payment "
        "remains due unless otherwise agreed in writing."
    )


@dataclass
class Services:
    """Services information data class"""

    performance_type: str = "themed stilt walker"
    duration_minutes: int = 4
    time_tbd: bool = True
    performance_time: str = "TBD"
    costume: str = "Caribbean-themed stilt costume"
    music_provided_by: str = "Client"
    music_notes: str = ""
    additional_services: str = ""


@dataclass
class Cancellation:
    """Cancellation policy data class"""

    client_policy: str = (
        "All payments are non-refundable.\n"
        "If Client cancels, Cirque Aflame will offer a backup date at no extra charge, subject to availability.\n"
        "If the backup date is not suitable, deposit may be applied to a future event within 12 months."
    )
    producer_policy: str = (
        "If the Producer cancels, a full refund will be provided or payment may be applied toward rescheduling."
    )
    force_majeure: str = (
        "Neither party shall be liable for failure to perform due to events beyond their reasonable control, "
        "including but not limited to: natural disasters, severe weather, civil unrest, pandemics, government "
        "restrictions, or other similar circumstances.\n\n"
        "In such cases, parties shall work together to reschedule the performance or find an equitable solution."
    )


@dataclass
class Schedule:
    """Schedule policy data class"""

    arrival_minutes_before: int = 30
    setup_minutes: int = 15
    late_policy: str = (
        "Performance fees are based on the agreed time and material costs.\n"
        "If the Client is late, Performer will accommodate if it doesn't interfere with other obligations.\n"
        "The full fee remains due even if performance is shortened at Client's request.\n"
        "If Performer arrives late, time will be made up if mutually agreed.\n"
        "Performer will wait 15 minutes past scheduled start time before considering it canceled per "
        "the cancellation policy."
    )
    changes_policy: str = (
        "Any changes to the performance date or time must be communicated as soon as possible.\n"
        "Changes requested within 48 hours of the event are subject to performer availability.\n"
        "If a change cannot be accommodated, the original agreement remains in effect or cancellation "
        "policies will apply."
    )


@dataclass
class Obligations:
    """Obligations data class"""

    producer_obligations: str = (
        "• Will ensure timely preparation and optimal performance delivery.\n"
        "• Will maintain confidentiality of Client information.\n"
        "• Will arrive with all necessary performance equipment and costumes.\n"
        "• May substitute another Cirque Aflame performer with Client's consent, if needed.\n"
        "• Will maintain professional conduct throughout the engagement.\n"
        "• Will collaborate with venue staff to ensure smooth integration."
    )
    client_obligations: str = (
        "• Will ensure a safe and hazard-free area for performance.\n"
        "• Will adhere to all terms and event setup responsibilities.\n"
        "• Will provide accurate information regarding venue, audience, and technical requirements.\n"
        "• Will ensure adequate space for performance and setup.\n"
        "• Will ensure that the venue permits the type of performance contracted.\n"
        "• Will inform Performer of any special circumstances that may affect the performance."
    )
    venue_requirements: str = (
        "• Performance area must have sufficient ceiling height for stilt walking (minimum 10 feet).\n"
        "• Floor surface must be smooth, level, and free of debris, cracks, or uneven surfaces.\n"
        "• A secure changing area must be provided for the Performer.\n"
        "• Adequate lighting for safe performance.\n"
        "• If outdoors, a covered area must be available in case of inclement weather."
    )


@dataclass
class Safety:
    """Health and safety data class"""

    general_safety_policy: str = (
        "Both parties agree to uphold safety as a priority.\n"
        "The Producer may modify or cancel the performance if conditions are unsafe.\n"
        "Full payment remains due if the Client is responsible for unsafe conditions."
    )
    specific_requirements: str = (
        "• Performance area must be free of obstacles and hazards.\n"
        "• If outdoors, performance will be modified or canceled in case of rain, strong winds, or extreme temperatures.\n"
        "• Performer reserves the right to refuse any activities deemed unsafe.\n"
        "• Audience must maintain a safe distance from performer on stilts.\n"
        "• Performer must have access to water and rest breaks as needed."
    )
    liability_terms: str = (
        "The Producer maintains appropriate liability insurance coverage for performance activities.\n\n"
        "Client acknowledges that performance arts carry inherent risks. Client agrees to indemnify and hold "
        "harmless the Producer and Performer from any claims, losses, or damages arising from the performance, "
        "except those caused by willful misconduct or gross negligence of the Producer or Performer.\n\n"
        "Each party shall be responsible for their own negligent acts or omissions."
    )


@dataclass
class Contract:
    """Complete contract data model"""

    title: str = "Caribbean Dance Performance Agreement"
    subtitle: str = "Official Contract for Live Performance Services"
    effective_date: str = datetime.datetime.now().strftime("%B %d, %Y")
    performer_name: str = "Robert Bershadsky"

    client: Client = field(default_factory=Client)
    producer: Producer = field(default_factory=Producer)
    event: Event = field(default_factory=Event)
    fees: Fees = field(default_factory=Fees)
    services: Services = field(default_factory=Services)
    cancellation: Cancellation = field(default_factory=Cancellation)
    schedule: Schedule = field(default_factory=Schedule)
    obligations: Obligations = field(default_factory=Obligations)
    safety: Safety = field(default_factory=Safety)

    def to_dict(self):
        """Convert contract to dictionary for serialization"""
        return asdict(self)

    @classmethod
    def from_dict(cls, data):
        """Create contract from dictionary"""
        # Handle nested dataclasses
        client = Client(**data.get("client", {}))
        producer = Producer(**data.get("producer", {}))
        event = Event(**data.get("event", {}))
        fees = Fees(**data.get("fees", {}))
        services = Services(**data.get("services", {}))
        cancellation = Cancellation(**data.get("cancellation", {}))
        schedule = Schedule(**data.get("schedule", {}))
        obligations = Obligations(**data.get("obligations", {}))
        safety = Safety(**data.get("safety", {}))

        # Create and return contract
        return cls(
            title=data.get("title", ""),
            subtitle=data.get("subtitle", ""),
            effective_date=data.get("effective_date", ""),
            performer_name=data.get("performer_name", ""),
            client=client,
            producer=producer,
            event=event,
            fees=fees,
            services=services,
            cancellation=cancellation,
            schedule=schedule,
            obligations=obligations,
            safety=safety,
        )

    def save_to_file(self, file_path):
        """Save contract to JSON file"""
        with open(file_path, "w") as f:
            json.dump(self.to_dict(), f, indent=2)

    def load_from_file(self, file_path):
        """Load contract from JSON file"""
        with open(file_path, "r") as f:
            data = json.load(f)

        # Convert dict to Contract
        contract = Contract.from_dict(data)

        # Update current object with loaded data
        self.__dict__.update(contract.__dict__)
