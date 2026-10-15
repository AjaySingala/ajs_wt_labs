from ticket_triage_starter import Ticket, classify_ticket

def test_critical_customer_sla_breach():
    t=Ticket("INC-TEST-1","Critical","P2",300,240,12000,"elevated response time")
    assert classify_ticket(t)["escalate"] is True

def test_low_impact_ticket():
    t=Ticket("INC-TEST-2","Medium","P4",30,2880,2,"documentation issue")
    assert classify_ticket(t)["escalate"] is False
