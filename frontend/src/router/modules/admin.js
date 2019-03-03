import Base from '@/components/admin/Base'

import Home from '@/components/admin/apps/home/Base'
import UsersTable from '@/components/admin/apps/users/Table'
import OficcesTable from '@/components/admin/apps/offices/Table'
import ClientTable from '@/components/admin/apps/clients/Table'
import AdsTable from '@/components/admin/apps/ads/Table'

export default {
  path: '/admin',
  component: Base,
  children: [
    { path: 'users', name: 'users', component: UsersTable },
    { path: 'offices', name: 'offices', component: OficcesTable },
    { path: 'clients', name: 'clients', component: ClientTable },
    { path: 'ads', name: 'ads', component: AdsTable },
    { path: '', name: 'home', component: Home }
  ]
}
