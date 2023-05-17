import Chat from '../pages/Chat';
import SignIn from '../pages/SignIn';
import SignUp from '../pages/SignUp';

// public routers
export const publicRouters = [
    { path: '/', component: SignIn, restricted: true },
    { path: '/signup', component: SignUp, restricted: true },
];

export const privateRouters = [{ path: '/chat', component: Chat }];

export * from './PrivateRoute.js';
export * from './PublicRoute.js';
