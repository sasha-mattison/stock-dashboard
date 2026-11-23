#pragma once

#include <wx/wx.h>

class App : public wxApp {
    private:

    public:
        bool OnInit() override;
};

class Frame : public wxFrame {
    public:
        Frame();
 
    private:
        void OnHello(wxCommandEvent& event);
        void OnExit(wxCommandEvent& event);
        void OnAbout(wxCommandEvent& event);
};