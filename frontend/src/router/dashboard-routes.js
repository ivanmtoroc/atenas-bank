import DashboardBase from '@/components/bases/DashboardBase'
import TableView from '@/components/views/TableView'

export default {
  path: '/dashboard',
  name: 'dashboard',
  component: DashboardBase,
  children: [
    {
      path: 'users',
      name: 'users',
      component: TableView
    }
  ]
}
