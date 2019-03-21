import Base from '@/components/admin/Base'

import Home from '@/components/admin/manager/apps/home/Base'
import UsersTable from '@/components/admin/manager/apps/users/Table'
import OficcesTable from '@/components/admin/manager/apps/offices/Table'
import ClientTable from '@/components/admin/manager/apps/clients/Table'
import AdsTable from '@/components/admin/manager/apps/ads/Table'

import Operator from '@/components/admin/operator/Base'

export default {
  path: '/admin',
  component: Base,
  children: [
    // Operator
    { path: 'operator', name: 'operator', component: Operator },
    // Manager
    { path: 'users', name: 'users', component: UsersTable },
    { path: 'offices', name: 'offices', component: OficcesTable },
    { path: 'clients', name: 'clients', component: ClientTable },
    { path: 'ads', name: 'ads', component: AdsTable },
    { path: '', name: 'home', component: Home }
  ]
}
