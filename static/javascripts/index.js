$(function()
    { $("#i_vol_up").click(function (event)
        { $.getJSON('/vol_up', { },
            function(data) { }); return false; }); });

$(function()
    { $("#i_vol_down").click(function (event)
        { $.getJSON('/vol_down', { },
            function(data) { }); return false; }); });

$(function()
    { $("#i_play_pause").click(function (event)
        { $.getJSON('/play_pause', { },
            function(data) { }); return false; }); });

$(function()
    { $("#i_reverse").click(function (event)
        { $.getJSON('/reverse', { },
            function(data) { }); return false; }); });

$(function()
    { $("#i_forward").click(function (event)
        { $.getJSON('/forward', { },
            function(data) { }); return false; }); });

$(function()
    { $("#i_previous_track").click(function (event)
        { $.getJSON('/previous_track', { },
            function(data) { }); return false; }); });

$(function()
    { $("#i_next_track").click(function (event)
        { $.getJSON('/next_track', { },
            function(data) { }); return false; }); });

$(function()
    { $("#i_youtube_previous_track").click(function (event)
        { $.getJSON('/youtube_previous_track', { },
            function(data) { }); return false; }); });

$(function()
    { $("#i_youtube_next_track").click(function (event)
        { $.getJSON('/youtube_next_track', { },
            function(data) { }); return false; }); });

$(function()
    { $("#i_youtube_playback_speed_plus").click(function (event)
        { $.getJSON('/youtube_playback_speed_plus', { },
            function(data) { }); return false; }); });

$(function()
    { $("#i_youtube_playback_speed_minus").click(function (event)
        { $.getJSON('/youtube_playback_speed_minus', { },
            function(data) { }); return false; }); });