<?php

namespace ATChallenge\Http\Middleware;

use Closure;
use Illuminate\Support\Facades\Auth;

class RedirectIfAuthenticated
{
    /**
     * Handle an incoming request.
     *
     * @param  \Illuminate\Http\Request  $request
     * @param  \Closure  $next
     * @param  string|null  $guard
     * @return mixed
     */
    public function handle($request, Closure $next, $guard = 'chairperson')
    {
        if (Auth::guard($guard)->check()) {
            return $next($request);
        }else{
            return redirect('/chairperson/login');
        }


    }
}
