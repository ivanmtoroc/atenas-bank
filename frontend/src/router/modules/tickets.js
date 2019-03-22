import Base from '@/components/tickets/Base'

import Services from '@/components/tickets/views/Services'
import Identification from '@/components/tickets/views/Identification'
import Tickets from '@/components/tickets/views/Tickets'
import Ticket from '@/components/tickets/views/Ticket'

export default {
  path: '/tickets',
  component: Base,
  children: [
    { path: '', name: 'tickets', component: Services },
    { path: 'identification', name: 'identification', component: Identification },
    { path: 'ticket', name: 'ticket', component: Ticket },
    { path: 'list', name: 'list', component: Tickets }
  ]
}
