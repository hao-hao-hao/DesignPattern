from models import Customer
from models import Fashion_newsletter

fashion_newsletter = Fashion_newsletter()
ken = Customer('ken')
jay = Customer('jay')

fashion_newsletter.add_subscriber(ken)
fashion_newsletter.add_subscriber(jay)
fashion_newsletter.notify_subscribers("Free Fashion Show Ticket")
fashion_newsletter.notify_subscribers("ABC is coming to the town")
