@extends('layout.app_admin')

@section('content')
    <div class="ui stackable grid">
        <div class="three wide column"></div>
        <div class="ten wide column">
            <div class="ui segments">
                <div class="ui segment">
                    <i class="large icons"><i class="user icon"></i><i class="corner lock icon"></i></i>Login
                </div>
                <div class="ui teal segment">
                    <div class="ui info message">
                        <p>Call: 0711222333 for Support or Email: ict@system.com</p>
                    </div>
                    @if(count($errors)>0)
                        <div class="ui error message">
                            <ol>
                                @foreach($errors->all() as $error)
                                    <li>{{$error}}</li>
                                @endforeach
                            </ol>
                        </div>
                    @endif
                    <form class="ui big form" action="/chairperson/register" method="POST">
                        {{csrf_field()}}

                        <div class="field">
                            <div class="ui left icon input">
                                <input type="text" name="name" placeholder="Name">
                                <i class="user icon"></i>
                            </div>
                        </div>
                        <div class="field">
                            <div class="ui left icon input">
                                <input type="text" name="email" placeholder="Email">
                                <i class="mail icon"></i>
                            </div>
                        </div>
                        <div class="field">
                            <div class="ui left icon input">
                                <input type="password" name="password" placeholder="Password">
                                <i class="lock icon"></i>
                            </div>
                        </div>
                        <div class="field">
                            <div class="ui left icon input">
                                <input type="password" name="password-confirm" placeholder="Confirm Password">
                                <i class="lock icon"></i>
                            </div>
                        </div>
                        <div class="field">
                            <button type="submit" class="ui big blue fluid button">Register</button>
                        </div>
                    </form>

                </div>
            </div>
        </div>
        <div class="three wide column"></div>
    </div>
@endsection
