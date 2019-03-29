package com.USSD;


import com.africastalking.ActionBuilder;
import com.africastalking.AfricasTalking;
import com.africastalking.Logger;
import com.africastalking.SmsService;
import com.africastalking.voice.action.GetDigits;
import com.africastalking.voice.action.Redirect;
import com.africastalking.voice.action.Reject;
import com.africastalking.voice.action.Say;
import com.google.gson.Gson;
import org.eclipse.jetty.server.Server;
import spark.ModelAndView;
import spark.template.handlebars.HandlebarsTemplateEngine;

import java.io.IOException;
import java.net.Inet4Address;
import java.net.InetAddress;
import java.net.URL;
import java.net.URLDecoder;
import java.util.HashMap;
import java.util.Map;

import static spark.Spark.*;

public class App {

    private static final int HTTP_PORT = 8080;
    private static final int RPC_PORT = 35897;
    private static final String USERNAME = "sandbox";
    private static final String API_KEY = "5430f51634741fcfeb2e51cc8f707a8e59a0586ba38811233157b6185b71281b";

    private static Gson gson = new Gson();

    private static HandlebarsTemplateEngine hbs = new HandlebarsTemplateEngine("/views");
    private static Server server;
    private static SmsService sms;


    private static void log(String message) {
        System.out.println(message);
    }

    private static void setupAfricastalking() throws IOException {
        // SDK Server
        AfricasTalking.initialize(USERNAME, API_KEY);
        AfricasTalking.setLogger(new Logger(){
            @Override
            public void log(String message, Object... args) {
                System.out.println(message);
            }
        });
        sms = AfricasTalking.getService(AfricasTalking.SERVICE_SMS);
        server = new Server();
        try{
        server.start();
        } catch (Exception e){
            System.exit(1);
        }

    }

    public static void main(String[] args) throws IOException {

        InetAddress host = Inet4Address.getLocalHost();
        log("\n");
        log(String.format("SDK Server: %s:%d", host.getHostAddress(), RPC_PORT));
        log(String.format("HTTP Server: %s:%d", host.getHostAddress(), HTTP_PORT));
        log("\n");
        HashMap<String, String> states = new HashMap<>();
        String baseUrl = "http://savvyprogrammer.io";

        setupAfricastalking();
        port(HTTP_PORT);

        staticFiles.location("/public");
        exception(Exception.class, (e, req, res) -> e.printStackTrace()); // print all exceptions

        get("/", (req, res) -> {
            Map<String, Object> data = new HashMap<>();
            data.put("req", req.pathInfo());
            return render("index", data);
        });

        post("/voice", (req, res) -> {

            // Parse POST data
            String[] raw = URLDecoder.decode(req.body()).split("&");
            Map<String, String> data = new HashMap<>();
            for (String item: raw) {
                String [] kw = item.split("=");
                if (kw.length == 2) {
                    data.put(kw[0], kw[1]);
                }
            }

            // Prep state
            boolean isActive = data.get("isActive").contentEquals("1");
            String sessionId = data.get("sessionId");
            String callerNumber = data.get("callerNumber");
            String dtmf = data.get("dtmfDigits");
            String state = isActive ? states.getOrDefault(sessionId, "menu") : "";

            ActionBuilder response = new ActionBuilder();

            switch (state) {
                case "menu":
                    states.put(sessionId, "process");
                    response.getDigits(new GetDigits(new Say("Enter your Username"), 1, "#", null));
                    response.getDigits(new GetDigits(new Say("Enter your Email"), 1, "#", null));
                    response.redirect(new Redirect(new URL(baseUrl + "/voice")));
                    break;
                default:
                    response.say(new Say("Well, this is unexpected! Bye Bye, Long Live Our Machine Overlords")).reject(new Reject());
                    break;
            }

            return response.build();
        });
        // Send SMS
        post("/auth/register/:phone", (req, res) -> sms.send("You have registered successfully", "AT2FA", new String[] {req.params("phone")}, false), gson::toJson);
    }

    private static String render(String view, Map data) {
        return hbs.render(new ModelAndView(data, view + ".hbs"));
    }

}
