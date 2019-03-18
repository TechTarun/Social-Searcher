package com.sample.boot.controller;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.servlet.mvc.support.RedirectAttributes;

import java.io.*;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.LinkedHashMap;

@Controller
public class MainController {

    @Value("${file.upload-dir}")
    String upload_dir;

    @Value("${api.search.script.path.facebook}")
    String search_api_path_facebook;

    @Value("${scraper.script.path.facebook}")
    String facebook_scraper_path;

    @Value("${image.matcher.path}")
    String image_matcher_path;

    @Value("${linkedin.scraper.path}")
    String linkedin_scraper_path;

    @Value("${facebook_output_dir}")
    String facebook_output_directory;

    @Value("${linkedin_output_dir}")
    String linkedin_output_directory;



    @RequestMapping("/")
    public String getHome(){
        return "Brand_Engagement";
    }

    @RequestMapping("/Corporate_Relationship")
    public String getCorporateRelationship(){
        return "Corporate_Relationship";
    }

    @RequestMapping("/Customer_Outreach")
    public String getCustomerOutreach(){
        return "Customer_Outreach";
    }

    @RequestMapping("/image_search")
    public String getImageSearch(Model model){
        String[] options={"a","b","c"};
        model.addAttribute("options",options);
        return "image_search";
    }

    @RequestMapping("/Customer_Classifier")
    public String getCustomerClassifier(){
        return "Customer_Classifier";
    }

    @RequestMapping("New_Customers")
    public String getNewCustomers(){
        return "New_Customers";
    }

    @RequestMapping("/Brand_Engagement")
    public String getBrandEngagement(){
        return "Brand_Engagement";
    }

    @RequestMapping("/social_finder")
    public String getSocialFinder(){
        return "social_finder";
    }

    @PostMapping("/image_search")
    public String postImageSearch(@RequestParam("file") MultipartFile file,@RequestParam("name") String name,@RequestParam("socialmedia") String socialmedia,RedirectAttributes redirectAttributes,Model model){

        File resultfile=null;
        String search_command="";
        String scraper_command="";
        String image_matcher_command="";
        String image_path="";

        if (file.isEmpty()) {
            redirectAttributes.addFlashAttribute("message", "Please select a file to upload");
            return "redirect:/image_search";
        }

        try {
            image_path=upload_dir +"/" +file.getOriginalFilename();
            // Get the file and save it somewhere
            byte[] bytes = file.getBytes();
            Path path = Paths.get(upload_dir +"/" +file.getOriginalFilename());
            Files.write(path, bytes);

            redirectAttributes.addFlashAttribute("message",
                    "You successfully uploaded '" + file.getOriginalFilename() + "'");

        } catch (IOException e) {
            e.printStackTrace();
        }
        System.out.println("Image will be searched for:"+name + "for platform:"+socialmedia);
        try {
            if("facebook".equalsIgnoreCase(socialmedia)) {
                search_command = "python3 " + search_api_path_facebook + " " + name;
                scraper_command = "python3 " + facebook_scraper_path;
                image_matcher_command="python3 " + image_matcher_path + " " + image_path + " " + facebook_output_directory + " " + socialmedia;
                resultfile = new File(facebook_output_directory+"result.txt");
            }else if("linkedin".equalsIgnoreCase(socialmedia)){
                search_command = "";
                scraper_command = "python3 " + linkedin_scraper_path + " " + name;
                image_matcher_command="python3 " + image_matcher_path + " " + image_path + " " + linkedin_output_directory + " " + socialmedia;
                resultfile = new File(linkedin_output_directory+"result.txt");
            }
            if(search_command != "") {
                String line;
                System.out.println("Command : " + search_command);
                Process search_api = Runtime.getRuntime().exec(search_command);
                BufferedReader search_buffer = new BufferedReader(new InputStreamReader(search_api.getInputStream()));

                while ((line = search_buffer.readLine()) != null) {
                    System.out.println(line);
                }
                InputStream search_error = search_api.getErrorStream();
                InputStreamReader isr_search_error = new InputStreamReader(search_error);
                BufferedReader search_image_buffer = new BufferedReader(isr_search_error);
                String line10;
                while ((line10 = search_image_buffer.readLine()) != null) {
                    System.out.println(line10);
                }
                search_api.waitFor();
                search_api.destroyForcibly();
                search_buffer.close();
            }

            if(scraper_command !="")
            {
                String line;
                Process facebook_processor=Runtime.getRuntime().exec(scraper_command);
                BufferedReader facebook_buffer=new BufferedReader(new InputStreamReader(facebook_processor.getInputStream()));
                while ((line = facebook_buffer.readLine()) != null) {
                    System.out.println(line);
                }
                InputStream search_buffer1 = facebook_processor.getErrorStream();
                InputStreamReader isr = new InputStreamReader(search_buffer1);
                BufferedReader image_buffer = new BufferedReader(isr);
                String line3;
                while ((line3 = image_buffer.readLine()) != null) {
                    System.out.println(line3);
                }
                facebook_processor.waitFor();
                facebook_processor.destroyForcibly();
                facebook_buffer.close();

                System.out.println(image_matcher_command);

                Process image_matcher=Runtime.getRuntime().exec(image_matcher_command);
                InputStream error = image_matcher.getErrorStream();
                InputStreamReader isr1 = new InputStreamReader(error);
                BufferedReader errorreader=new BufferedReader(isr1);
                BufferedReader image_buffer2=new BufferedReader(new InputStreamReader(image_matcher.getInputStream()));
                String line2;
                while ((line2 = image_buffer2.readLine()) != null) {
                    System.out.println(line2);
                }
                String line4;
                while ((line4 = errorreader.readLine()) != null) {
                    System.out.println(line4);
                }
                image_matcher.waitFor();
                image_matcher.destroyForcibly();
                image_buffer.close();

                BufferedReader br = new BufferedReader(new FileReader(resultfile));
                String st=br.readLine();
                if( br.readLine()!= null)
                {
                    st=st+br.readLine();
                }
                System.out.println(st);
                model.addAttribute("message",st);
            }
        }catch(Exception ex){
            System.out.println("Exception"+ex);
            return "redirect:/image_search";
        }
        return "redirect:/image_search";
    }
}
