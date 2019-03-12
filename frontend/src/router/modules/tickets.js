import Base from '@/components/tickets/Base'

import Home from '@/components/tickets/views/Home'
import Tickets from '@/components/tickets/views/Tickets'

export default {
  path: '/tickets',
  component: Base,
  children: [
    { path: 'list', name: 'list', component: Tickets },
    { path: '', name: 'tickets', component: Home }
  ]
}
